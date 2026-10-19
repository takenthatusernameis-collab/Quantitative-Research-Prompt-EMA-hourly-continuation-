# EMA Hourly Continuation — SEI/USDT P12_144

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.7913 |
| net_win_rate | 0.5155 |
| gross_profit_factor | 1.1052 |
| gross_win_rate | 0.5259 |
| sharpe_ratio | -1.4727 |
| sortino_ratio | -0.4078 |
| max_drawdown | 0.4250 |
| cagr | -0.1779 |
| net_avg_win | 74.0495 |
| net_avg_loss | -99.5802 |
| avg_hold_time_bars | 41.4534 |
| exposure | 0.7273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
