# EMA Hourly Continuation — TRX/USDT P8_50

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.5670 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 1.0643 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -5.2171 |
| sortino_ratio | -1.8872 |
| max_drawdown | 0.8934 |
| cagr | -0.5807 |
| net_avg_win | 37.6033 |
| net_avg_loss | -64.8475 |
| avg_hold_time_bars | 14.7840 |
| exposure | 0.4200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
