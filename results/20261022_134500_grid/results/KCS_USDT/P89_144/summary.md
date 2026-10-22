# EMA Hourly Continuation — KCS/USDT P89_144

**Symbol:** KCS/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.1776 |
| net_win_rate | 0.3596 |
| gross_profit_factor | 0.5906 |
| gross_win_rate | 0.4173 |
| sharpe_ratio | -9.4448 |
| sortino_ratio | -3.1472 |
| max_drawdown | 0.9853 |
| cagr | -0.8125 |
| net_avg_win | 11.3756 |
| net_avg_loss | -35.9694 |
| avg_hold_time_bars | 5.7635 |
| exposure | 0.1362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
