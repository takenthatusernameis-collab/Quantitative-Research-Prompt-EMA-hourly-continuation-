# EMA Hourly Continuation — CSPR/USDT P34_55

**Symbol:** CSPR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1183 |
| net_profit_factor | 0.2863 |
| net_win_rate | 0.3795 |
| gross_profit_factor | 0.6825 |
| gross_win_rate | 0.4032 |
| sharpe_ratio | -11.7177 |
| sortino_ratio | -5.7284 |
| max_drawdown | 0.9994 |
| cagr | -0.9470 |
| net_avg_win | 8.9273 |
| net_avg_loss | -19.0765 |
| avg_hold_time_bars | 2.7227 |
| exposure | 0.1464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
