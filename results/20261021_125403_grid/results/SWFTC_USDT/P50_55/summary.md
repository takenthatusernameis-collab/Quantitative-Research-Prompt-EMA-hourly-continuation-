# EMA Hourly Continuation — SWFTC/USDT P50_55

**Symbol:** SWFTC/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 91 |
| net_profit_factor | 0.5778 |
| net_win_rate | 0.4396 |
| gross_profit_factor | 0.7927 |
| gross_win_rate | 0.4396 |
| sharpe_ratio | -1.6475 |
| sortino_ratio | -0.2237 |
| max_drawdown | 0.2534 |
| cagr | -0.0977 |
| net_avg_win | 77.8062 |
| net_avg_loss | -105.6205 |
| avg_hold_time_bars | 6.4725 |
| exposure | 0.0268 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
