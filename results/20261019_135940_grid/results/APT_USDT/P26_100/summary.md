# EMA Hourly Continuation — APT/USDT P26_100

**Symbol:** APT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.5828 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9532 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -4.5920 |
| sortino_ratio | -1.6732 |
| max_drawdown | 0.8741 |
| cagr | -0.5541 |
| net_avg_win | 38.6347 |
| net_avg_loss | -58.3078 |
| avg_hold_time_bars | 11.6036 |
| exposure | 0.3539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
