# EMA Hourly Continuation — YFI/USDT P12_20

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.4145 |
| net_win_rate | 0.4289 |
| gross_profit_factor | 0.7367 |
| gross_win_rate | 0.4289 |
| sharpe_ratio | -5.3199 |
| sortino_ratio | -1.5752 |
| max_drawdown | 0.8488 |
| cagr | -0.5183 |
| net_avg_win | 32.9216 |
| net_avg_loss | -59.6466 |
| avg_hold_time_bars | 5.2251 |
| exposure | 0.0998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
