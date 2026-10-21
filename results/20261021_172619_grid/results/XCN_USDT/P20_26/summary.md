# EMA Hourly Continuation — XCN/USDT P20_26

**Symbol:** XCN/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 174 |
| net_profit_factor | 0.8043 |
| net_win_rate | 0.5345 |
| gross_profit_factor | 1.1541 |
| gross_win_rate | 0.5345 |
| sharpe_ratio | -0.9368 |
| sortino_ratio | -0.1785 |
| max_drawdown | 0.2720 |
| cagr | -0.0793 |
| net_avg_win | 82.8153 |
| net_avg_loss | -118.2132 |
| avg_hold_time_bars | 5.3276 |
| exposure | 0.0421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
