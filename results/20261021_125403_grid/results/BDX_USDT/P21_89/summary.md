# EMA Hourly Continuation — BDX/USDT P21_89

**Symbol:** BDX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.5840 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.9169 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -3.7242 |
| sortino_ratio | -1.0982 |
| max_drawdown | 0.7373 |
| cagr | -0.3991 |
| net_avg_win | 50.6699 |
| net_avg_loss | -77.1176 |
| avg_hold_time_bars | 11.6776 |
| exposure | 0.2256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
