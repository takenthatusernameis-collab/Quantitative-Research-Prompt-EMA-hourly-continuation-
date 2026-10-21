# EMA Hourly Continuation — ZEC/USDT P89_100

**Symbol:** ZEC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 85 |
| net_profit_factor | 0.7841 |
| net_win_rate | 0.5176 |
| gross_profit_factor | 1.0570 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -0.6469 |
| sortino_ratio | -0.0860 |
| max_drawdown | 0.1102 |
| cagr | -0.0385 |
| net_avg_win | 77.5798 |
| net_avg_loss | -106.1761 |
| avg_hold_time_bars | 4.5176 |
| exposure | 0.0175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
