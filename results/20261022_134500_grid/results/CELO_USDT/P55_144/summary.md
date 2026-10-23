# EMA Hourly Continuation — CELO/USDT P55_144

**Symbol:** CELO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.6586 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 1.0175 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -2.6831 |
| sortino_ratio | -0.8054 |
| max_drawdown | 0.6178 |
| cagr | -0.3146 |
| net_avg_win | 53.6224 |
| net_avg_loss | -78.9212 |
| avg_hold_time_bars | 12.2383 |
| exposure | 0.2487 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
