# EMA Hourly Continuation — STX/USDT P12_200

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.8514 |
| net_win_rate | 0.5060 |
| gross_profit_factor | 1.0057 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -0.7475 |
| sortino_ratio | -0.1682 |
| max_drawdown | 0.2625 |
| cagr | -0.0765 |
| net_avg_win | 82.7865 |
| net_avg_loss | -99.6020 |
| avg_hold_time_bars | 70.5743 |
| exposure | 0.7952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
