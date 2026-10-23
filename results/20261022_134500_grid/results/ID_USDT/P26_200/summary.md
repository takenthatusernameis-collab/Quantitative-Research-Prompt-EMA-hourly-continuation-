# EMA Hourly Continuation — ID/USDT P26_200

**Symbol:** ID/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.6767 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9145 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -2.0332 |
| sortino_ratio | -0.5445 |
| max_drawdown | 0.4816 |
| cagr | -0.2256 |
| net_avg_win | 57.1852 |
| net_avg_loss | -79.4797 |
| avg_hold_time_bars | 36.3872 |
| exposure | 0.5912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
