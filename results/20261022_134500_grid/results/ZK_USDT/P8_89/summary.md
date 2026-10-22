# EMA Hourly Continuation — ZK/USDT P8_89

**Symbol:** ZK/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 738 |
| net_profit_factor | 0.7131 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9979 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -3.4804 |
| sortino_ratio | -1.3806 |
| max_drawdown | 0.7934 |
| cagr | -0.4796 |
| net_avg_win | 54.6892 |
| net_avg_loss | -71.4732 |
| avg_hold_time_bars | 17.3699 |
| exposure | 0.6250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
