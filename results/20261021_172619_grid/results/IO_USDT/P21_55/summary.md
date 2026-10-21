# EMA Hourly Continuation — IO/USDT P21_55

**Symbol:** IO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7921 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9657 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -1.6555 |
| sortino_ratio | -0.5139 |
| max_drawdown | 0.4486 |
| cagr | -0.2115 |
| net_avg_win | 75.3000 |
| net_avg_loss | -91.2791 |
| avg_hold_time_bars | 8.6772 |
| exposure | 0.1861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
