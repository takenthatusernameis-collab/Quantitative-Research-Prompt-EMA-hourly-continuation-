# EMA Hourly Continuation — TIA/USDT P8_89

**Symbol:** TIA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.7488 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 1.0302 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -2.5544 |
| sortino_ratio | -0.9215 |
| max_drawdown | 0.6937 |
| cagr | -0.3557 |
| net_avg_win | 61.1307 |
| net_avg_loss | -80.8893 |
| avg_hold_time_bars | 22.3817 |
| exposure | 0.6664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
