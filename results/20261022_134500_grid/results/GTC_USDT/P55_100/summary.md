# EMA Hourly Continuation — GTC/USDT P55_100

**Symbol:** GTC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.5589 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9353 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -4.5426 |
| sortino_ratio | -1.5946 |
| max_drawdown | 0.8633 |
| cagr | -0.5310 |
| net_avg_win | 37.0376 |
| net_avg_loss | -59.5199 |
| avg_hold_time_bars | 6.4146 |
| exposure | 0.1793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
