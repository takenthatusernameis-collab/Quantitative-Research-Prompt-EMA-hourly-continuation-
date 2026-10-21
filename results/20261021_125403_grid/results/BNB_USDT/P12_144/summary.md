# EMA Hourly Continuation — BNB/USDT P12_144

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.6305 |
| net_win_rate | 0.4910 |
| gross_profit_factor | 0.9301 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -2.6250 |
| sortino_ratio | -0.7403 |
| max_drawdown | 0.5862 |
| cagr | -0.2864 |
| net_avg_win | 51.3331 |
| net_avg_loss | -78.5199 |
| avg_hold_time_bars | 35.4522 |
| exposure | 0.6236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
