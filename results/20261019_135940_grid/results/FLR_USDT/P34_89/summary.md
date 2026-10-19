# EMA Hourly Continuation — FLR/USDT P34_89

**Symbol:** FLR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 854 |
| net_profit_factor | 0.4262 |
| net_win_rate | 0.4098 |
| gross_profit_factor | 0.7921 |
| gross_win_rate | 0.4321 |
| sharpe_ratio | -8.1884 |
| sortino_ratio | -3.3806 |
| max_drawdown | 0.9852 |
| cagr | -0.8129 |
| net_avg_win | 20.9098 |
| net_avg_loss | -34.0673 |
| avg_hold_time_bars | 5.9848 |
| exposure | 0.2323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
