# EMA Hourly Continuation — ARPA/USDT P8_12

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.5852 |
| net_win_rate | 0.4696 |
| gross_profit_factor | 0.9367 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -4.1955 |
| sortino_ratio | -1.3387 |
| max_drawdown | 0.7908 |
| cagr | -0.4576 |
| net_avg_win | 47.8190 |
| net_avg_loss | -72.3543 |
| avg_hold_time_bars | 4.4757 |
| exposure | 0.1000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
