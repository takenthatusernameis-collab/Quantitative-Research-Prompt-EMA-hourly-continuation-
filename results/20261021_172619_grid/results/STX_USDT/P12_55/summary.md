# EMA Hourly Continuation — STX/USDT P12_55

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.7231 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9186 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -2.4049 |
| sortino_ratio | -0.8626 |
| max_drawdown | 0.6607 |
| cagr | -0.3269 |
| net_avg_win | 53.5669 |
| net_avg_loss | -70.2002 |
| avg_hold_time_bars | 12.3649 |
| exposure | 0.3542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
