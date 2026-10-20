# EMA Hourly Continuation — ZEN/USDT P20_144

**Symbol:** ZEN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.7641 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.1182 |
| gross_win_rate | 0.5232 |
| sharpe_ratio | -2.0904 |
| sortino_ratio | -0.6716 |
| max_drawdown | 0.6006 |
| cagr | -0.2752 |
| net_avg_win | 66.9890 |
| net_avg_loss | -93.9852 |
| avg_hold_time_bars | 23.1853 |
| exposure | 0.5459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
