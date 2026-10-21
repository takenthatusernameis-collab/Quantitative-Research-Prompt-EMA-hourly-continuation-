# EMA Hourly Continuation — ETH/USDT P21_89

**Symbol:** ETH/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6948 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 0.9878 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -2.2158 |
| sortino_ratio | -0.6156 |
| max_drawdown | 0.5366 |
| cagr | -0.2457 |
| net_avg_win | 61.7795 |
| net_avg_loss | -87.9725 |
| avg_hold_time_bars | 22.3511 |
| exposure | 0.3820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
