# EMA Hourly Continuation — FET/USDT P50_144

**Symbol:** FET/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.6899 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0140 |
| gross_win_rate | 0.5110 |
| sharpe_ratio | -2.3040 |
| sortino_ratio | -0.6898 |
| max_drawdown | 0.5911 |
| cagr | -0.2806 |
| net_avg_win | 54.6543 |
| net_avg_loss | -80.6302 |
| avg_hold_time_bars | 13.9537 |
| exposure | 0.2880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
