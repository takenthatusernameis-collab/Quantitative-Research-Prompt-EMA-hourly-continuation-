# EMA Hourly Continuation — XEC/USDT P34_144

**Symbol:** XEC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.6113 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.9169 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -3.7748 |
| sortino_ratio | -1.2236 |
| max_drawdown | 0.7804 |
| cagr | -0.4419 |
| net_avg_win | 49.2426 |
| net_avg_loss | -69.7774 |
| avg_hold_time_bars | 17.8113 |
| exposure | 0.4272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
