# EMA Hourly Continuation — XCN/USDT P21_144

**Symbol:** XCN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.5222 |
| net_win_rate | 0.4302 |
| gross_profit_factor | 0.8234 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -5.8731 |
| sortino_ratio | -2.1825 |
| max_drawdown | 0.9304 |
| cagr | -0.6537 |
| net_avg_win | 33.6649 |
| net_avg_loss | -48.6741 |
| avg_hold_time_bars | 15.5627 |
| exposure | 0.4966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
