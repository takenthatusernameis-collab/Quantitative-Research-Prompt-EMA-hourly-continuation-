# EMA Hourly Continuation — TIA/USDT P26_34

**Symbol:** TIA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 175 |
| net_profit_factor | 0.6566 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.8669 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -1.6755 |
| sortino_ratio | -0.3164 |
| max_drawdown | 0.3385 |
| cagr | -0.1346 |
| net_avg_win | 71.0121 |
| net_avg_loss | -95.3546 |
| avg_hold_time_bars | 5.1200 |
| exposure | 0.0407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
