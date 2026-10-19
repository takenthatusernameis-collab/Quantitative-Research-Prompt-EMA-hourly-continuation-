# EMA Hourly Continuation — WIF/USDT P20_144

**Symbol:** WIF/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.6444 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8705 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -3.0681 |
| sortino_ratio | -0.9511 |
| max_drawdown | 0.6843 |
| cagr | -0.3647 |
| net_avg_win | 54.5198 |
| net_avg_loss | -72.9804 |
| avg_hold_time_bars | 25.1311 |
| exposure | 0.5575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
