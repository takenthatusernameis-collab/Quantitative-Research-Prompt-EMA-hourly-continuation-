# EMA Hourly Continuation — GMEE/USDT P89_144

**Symbol:** GMEE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.3863 |
| net_win_rate | 0.3883 |
| gross_profit_factor | 0.5963 |
| gross_win_rate | 0.3928 |
| sharpe_ratio | -5.7369 |
| sortino_ratio | -1.7033 |
| max_drawdown | 0.8805 |
| cagr | -0.5643 |
| net_avg_win | 32.0522 |
| net_avg_loss | -52.6619 |
| avg_hold_time_bars | 5.8984 |
| exposure | 0.1188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
