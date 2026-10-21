# EMA Hourly Continuation — BNB/USDT P100_144

**Symbol:** BNB/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.5789 |
| net_win_rate | 0.5422 |
| gross_profit_factor | 1.1350 |
| gross_win_rate | 0.5422 |
| sharpe_ratio | -2.2444 |
| sortino_ratio | -0.4898 |
| max_drawdown | 0.4307 |
| cagr | -0.1984 |
| net_avg_win | 48.0259 |
| net_avg_loss | -98.2576 |
| avg_hold_time_bars | 6.3422 |
| exposure | 0.0649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
