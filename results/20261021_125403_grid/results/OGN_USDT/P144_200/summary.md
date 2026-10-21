# EMA Hourly Continuation — OGN/USDT P144_200

**Symbol:** OGN/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.7036 |
| net_win_rate | 0.5105 |
| gross_profit_factor | 1.0327 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -1.7445 |
| sortino_ratio | -0.4227 |
| max_drawdown | 0.4111 |
| cagr | -0.1762 |
| net_avg_win | 62.8866 |
| net_avg_loss | -93.2118 |
| avg_hold_time_bars | 6.5769 |
| exposure | 0.0851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
