# EMA Hourly Continuation — STX/USDT P144_200

**Symbol:** STX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 173 |
| net_profit_factor | 0.8592 |
| net_win_rate | 0.5376 |
| gross_profit_factor | 1.1475 |
| gross_win_rate | 0.5376 |
| sharpe_ratio | -0.5750 |
| sortino_ratio | -0.1091 |
| max_drawdown | 0.1769 |
| cagr | -0.0500 |
| net_avg_win | 79.6961 |
| net_avg_loss | -107.8286 |
| avg_hold_time_bars | 8.0636 |
| exposure | 0.0631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
