# EMA Hourly Continuation — DUSK/USDT P20_55

**Symbol:** DUSK/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.5933 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.9513 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -6.1258 |
| sortino_ratio | -2.6195 |
| max_drawdown | 0.9617 |
| cagr | -0.7153 |
| net_avg_win | 33.8223 |
| net_avg_loss | -46.0710 |
| avg_hold_time_bars | 5.5541 |
| exposure | 0.2333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
