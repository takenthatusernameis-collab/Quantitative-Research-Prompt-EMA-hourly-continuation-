# EMA Hourly Continuation — ERG/USDT P20_21

**Symbol:** ERG/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1256 |
| net_profit_factor | 0.0792 |
| net_win_rate | 0.2118 |
| gross_profit_factor | 0.3076 |
| gross_win_rate | 0.2779 |
| sharpe_ratio | -21.2145 |
| sortino_ratio | -11.9016 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 3.2327 |
| net_avg_loss | -10.9696 |
| avg_hold_time_bars | 1.8169 |
| exposure | 0.1037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
