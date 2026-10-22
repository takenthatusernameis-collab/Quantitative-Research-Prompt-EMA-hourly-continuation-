# EMA Hourly Continuation — XLM/USDT P21_89

**Symbol:** XLM/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.4543 |
| net_win_rate | 0.4761 |
| gross_profit_factor | 0.9431 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -5.2351 |
| sortino_ratio | -1.9182 |
| max_drawdown | 0.9169 |
| cagr | -0.6166 |
| net_avg_win | 23.0279 |
| net_avg_loss | -46.0652 |
| avg_hold_time_bars | 12.9262 |
| exposure | 0.4060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
