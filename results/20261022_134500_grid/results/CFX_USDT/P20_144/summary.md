# EMA Hourly Continuation — CFX/USDT P20_144

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.6581 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9616 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -2.9320 |
| sortino_ratio | -0.9230 |
| max_drawdown | 0.6914 |
| cagr | -0.3591 |
| net_avg_win | 52.4336 |
| net_avg_loss | -75.3982 |
| avg_hold_time_bars | 22.5846 |
| exposure | 0.5215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
