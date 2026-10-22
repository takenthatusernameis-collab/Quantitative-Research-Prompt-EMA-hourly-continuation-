# EMA Hourly Continuation — ETH/USDT P12_100

**Symbol:** ETH/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.4872 |
| net_win_rate | 0.4564 |
| gross_profit_factor | 0.9513 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -5.5521 |
| sortino_ratio | -1.8497 |
| max_drawdown | 0.9089 |
| cagr | -0.6124 |
| net_avg_win | 32.9117 |
| net_avg_loss | -56.7221 |
| avg_hold_time_bars | 22.7439 |
| exposure | 0.5934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
