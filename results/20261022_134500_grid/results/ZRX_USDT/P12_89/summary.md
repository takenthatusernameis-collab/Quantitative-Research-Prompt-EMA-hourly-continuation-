# EMA Hourly Continuation — ZRX/USDT P12_89

**Symbol:** ZRX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.5799 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.9031 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -4.5095 |
| sortino_ratio | -1.6177 |
| max_drawdown | 0.8677 |
| cagr | -0.5464 |
| net_avg_win | 38.9165 |
| net_avg_loss | -57.8460 |
| avg_hold_time_bars | 18.5764 |
| exposure | 0.5581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
