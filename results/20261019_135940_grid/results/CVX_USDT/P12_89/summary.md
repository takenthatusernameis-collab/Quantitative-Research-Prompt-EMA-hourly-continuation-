# EMA Hourly Continuation — CVX/USDT P12_89

**Symbol:** CVX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 753 |
| net_profit_factor | 0.5899 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.8506 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -3.9879 |
| sortino_ratio | -1.5284 |
| max_drawdown | 0.8453 |
| cagr | -0.5225 |
| net_avg_win | 34.0917 |
| net_avg_loss | -51.8239 |
| avg_hold_time_bars | 15.1195 |
| exposure | 0.5175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
