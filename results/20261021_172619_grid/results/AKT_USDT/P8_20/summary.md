# EMA Hourly Continuation — AKT/USDT P8_20

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6857 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.9019 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -2.6022 |
| sortino_ratio | -0.7966 |
| max_drawdown | 0.6393 |
| cagr | -0.3059 |
| net_avg_win | 60.3511 |
| net_avg_loss | -78.5949 |
| avg_hold_time_bars | 5.7913 |
| exposure | 0.1211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
