# EMA Hourly Continuation — BCH/USDT P20_34

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.5645 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.8431 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -3.0023 |
| sortino_ratio | -0.7341 |
| max_drawdown | 0.5721 |
| cagr | -0.2861 |
| net_avg_win | 55.2346 |
| net_avg_loss | -83.5160 |
| avg_hold_time_bars | 5.7079 |
| exposure | 0.0755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
