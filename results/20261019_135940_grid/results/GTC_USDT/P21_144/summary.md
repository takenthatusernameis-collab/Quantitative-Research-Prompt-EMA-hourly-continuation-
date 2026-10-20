# EMA Hourly Continuation — GTC/USDT P21_144

**Symbol:** GTC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.6443 |
| net_win_rate | 0.4566 |
| gross_profit_factor | 0.9127 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -3.4263 |
| sortino_ratio | -1.1104 |
| max_drawdown | 0.7579 |
| cagr | -0.4071 |
| net_avg_win | 54.7125 |
| net_avg_loss | -71.3538 |
| avg_hold_time_bars | 21.0717 |
| exposure | 0.5076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
