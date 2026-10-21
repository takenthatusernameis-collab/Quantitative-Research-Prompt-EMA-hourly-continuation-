# EMA Hourly Continuation — ICP/USDT P12_34

**Symbol:** ICP/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.7798 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0527 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -1.9062 |
| sortino_ratio | -0.6310 |
| max_drawdown | 0.5612 |
| cagr | -0.2516 |
| net_avg_win | 67.8205 |
| net_avg_loss | -90.3164 |
| avg_hold_time_bars | 6.2717 |
| exposure | 0.1511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
