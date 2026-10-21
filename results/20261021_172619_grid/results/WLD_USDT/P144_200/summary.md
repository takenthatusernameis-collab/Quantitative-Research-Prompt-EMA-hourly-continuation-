# EMA Hourly Continuation — WLD/USDT P144_200

**Symbol:** WLD/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.9232 |
| net_win_rate | 0.5389 |
| gross_profit_factor | 1.1560 |
| gross_win_rate | 0.5389 |
| sharpe_ratio | -0.2802 |
| sortino_ratio | -0.0524 |
| max_drawdown | 0.1040 |
| cagr | -0.0259 |
| net_avg_win | 85.3272 |
| net_avg_loss | -108.0283 |
| avg_hold_time_bars | 7.9042 |
| exposure | 0.0600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
