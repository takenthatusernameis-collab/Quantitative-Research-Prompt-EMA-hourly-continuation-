# EMA Hourly Continuation — STX/USDT P12_55

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1016 |
| net_profit_factor | 0.5260 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8525 |
| gross_win_rate | 0.4547 |
| sharpe_ratio | -6.6714 |
| sortino_ratio | -2.9622 |
| max_drawdown | 0.9775 |
| cagr | -0.7678 |
| net_avg_win | 23.7225 |
| net_avg_loss | -36.7253 |
| avg_hold_time_bars | 8.3179 |
| exposure | 0.3824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
