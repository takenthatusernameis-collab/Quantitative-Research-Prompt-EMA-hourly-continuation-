# EMA Hourly Continuation — KSM/USDT P34_89

**Symbol:** KSM/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.5392 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.9011 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -4.9392 |
| sortino_ratio | -1.8221 |
| max_drawdown | 0.8950 |
| cagr | -0.5838 |
| net_avg_win | 32.1187 |
| net_avg_loss | -53.7600 |
| avg_hold_time_bars | 7.8726 |
| exposure | 0.2444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
