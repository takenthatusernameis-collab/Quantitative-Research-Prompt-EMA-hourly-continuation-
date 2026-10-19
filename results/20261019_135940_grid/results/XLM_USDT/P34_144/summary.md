# EMA Hourly Continuation — XLM/USDT P34_144

**Symbol:** XLM/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.4719 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.8534 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -4.3541 |
| sortino_ratio | -1.3279 |
| max_drawdown | 0.8147 |
| cagr | -0.4839 |
| net_avg_win | 32.4601 |
| net_avg_loss | -59.6861 |
| avg_hold_time_bars | 17.8229 |
| exposure | 0.3889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
