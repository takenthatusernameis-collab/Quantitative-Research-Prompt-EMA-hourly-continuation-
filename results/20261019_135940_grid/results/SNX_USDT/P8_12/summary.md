# EMA Hourly Continuation — SNX/USDT P8_12

**Symbol:** SNX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1788 |
| net_profit_factor | 0.2378 |
| net_win_rate | 0.3753 |
| gross_profit_factor | 0.7888 |
| gross_win_rate | 0.4139 |
| sharpe_ratio | -16.9560 |
| sortino_ratio | -10.2826 |
| max_drawdown | 1.0000 |
| cagr | -0.9960 |
| net_avg_win | 4.6491 |
| net_avg_loss | -11.7454 |
| avg_hold_time_bars | 2.0218 |
| exposure | 0.1636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
