# EMA Hourly Continuation — XDC/USDT P20_50

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1050 |
| net_profit_factor | 0.1979 |
| net_win_rate | 0.3962 |
| gross_profit_factor | 0.5877 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -11.5948 |
| sortino_ratio | -5.3495 |
| max_drawdown | 0.9992 |
| cagr | -0.9404 |
| net_avg_win | 5.9267 |
| net_avg_loss | -19.6484 |
| avg_hold_time_bars | 4.6019 |
| exposure | 0.2196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
