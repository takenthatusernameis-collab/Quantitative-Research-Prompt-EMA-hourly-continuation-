# EMA Hourly Continuation — STX/USDT P8_50

**Symbol:** STX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1069 |
| net_profit_factor | 0.5900 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.9238 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -5.7973 |
| sortino_ratio | -2.6488 |
| max_drawdown | 0.9634 |
| cagr | -0.7235 |
| net_avg_win | 27.6521 |
| net_avg_loss | -41.1875 |
| avg_hold_time_bars | 9.8017 |
| exposure | 0.4741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
