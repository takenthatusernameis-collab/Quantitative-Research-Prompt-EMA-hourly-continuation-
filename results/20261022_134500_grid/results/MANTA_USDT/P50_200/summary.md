# EMA Hourly Continuation — MANTA/USDT P50_200

**Symbol:** MANTA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.7421 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9831 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -1.8069 |
| sortino_ratio | -0.4680 |
| max_drawdown | 0.4494 |
| cagr | -0.1956 |
| net_avg_win | 74.3168 |
| net_avg_loss | -97.1659 |
| avg_hold_time_bars | 31.8248 |
| exposure | 0.4788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
