# EMA Hourly Continuation — STX/USDT P50_89

**Symbol:** STX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.6387 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.8519 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -2.3792 |
| sortino_ratio | -0.6229 |
| max_drawdown | 0.5178 |
| cagr | -0.2483 |
| net_avg_win | 57.0609 |
| net_avg_loss | -79.3591 |
| avg_hold_time_bars | 7.4231 |
| exposure | 0.1135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
