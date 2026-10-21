# EMA Hourly Continuation — ENJ/USDT P34_89

**Symbol:** ENJ/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.8238 |
| net_win_rate | 0.5142 |
| gross_profit_factor | 1.0671 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -1.3616 |
| sortino_ratio | -0.4174 |
| max_drawdown | 0.4655 |
| cagr | -0.1756 |
| net_avg_win | 76.7129 |
| net_avg_loss | -98.5706 |
| avg_hold_time_bars | 10.9869 |
| exposure | 0.2272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
