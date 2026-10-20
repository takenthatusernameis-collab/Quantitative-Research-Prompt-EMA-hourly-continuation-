# EMA Hourly Continuation — YFI/USDT P21_144

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.5937 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 1.0062 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.9611 |
| sortino_ratio | -1.3029 |
| max_drawdown | 0.8179 |
| cagr | -0.4735 |
| net_avg_win | 43.0698 |
| net_avg_loss | -68.9934 |
| avg_hold_time_bars | 21.3889 |
| exposure | 0.5401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
