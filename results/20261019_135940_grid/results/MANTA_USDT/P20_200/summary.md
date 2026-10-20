# EMA Hourly Continuation — MANTA/USDT P20_200

**Symbol:** MANTA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.8722 |
| net_win_rate | 0.5292 |
| gross_profit_factor | 1.1507 |
| gross_win_rate | 0.5326 |
| sharpe_ratio | -0.7619 |
| sortino_ratio | -0.1844 |
| max_drawdown | 0.3176 |
| cagr | -0.0850 |
| net_avg_win | 88.5457 |
| net_avg_loss | -114.1202 |
| avg_hold_time_bars | 52.6323 |
| exposure | 0.6962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
